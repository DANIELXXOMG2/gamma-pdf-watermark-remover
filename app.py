import os
import tempfile
from pathlib import Path
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException
from werkzeug.utils import secure_filename
from watermark_detector import WatermarkDetector
from watermark_remover import WatermarkRemover

# Create necessary directories
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
ALLOWED_EXTENSIONS = {'pdf'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app = FastAPI(title="Gamma AI Watermark Remover", version="2.0.0")

# Template configuration
templates = Jinja2Templates(directory="templates")

# Initialize detector and remover
detector = WatermarkDetector()
remover = WatermarkRemover()

def allowed_file(filename: str) -> bool:
    """Checks allowed file type"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Main page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/remove_watermark")
async def remove_watermark(request: Request, pdf_file: UploadFile = File(...)):
    """Remove watermarks from PDF"""

    # File validation
    if not pdf_file.filename:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "error_message": "No file selected. Please choose a PDF file."}
        )

    if not allowed_file(pdf_file.filename):
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "error_message": "Invalid file type. Please upload a PDF file."}
        )

    # Secure filename
    filename = secure_filename(pdf_file.filename)

    # Create temporary files
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_input:
        upload_path = temp_input.name

        try:
            # Save uploaded file
            content = await pdf_file.read()
            temp_input.write(content)
            temp_input.flush()

            # Identify elements to remove
            print(f"Analyzing file: {filename}")
            elements_to_remove, error = detector.identify_watermarks(upload_path)

            if error:
                raise Exception(error)

            if elements_to_remove:
                # Create output filename
                output_filename = f'processed_{filename}'
                output_path = os.path.join(OUTPUT_FOLDER, output_filename)

                # Remove watermarks using new algorithm
                print(f"Removing watermarks...")
                images_removed, links_removed = remover.clean_pdf_from_target_domain(upload_path, output_path)

                total_removed = images_removed + links_removed
                success_message = f'Watermarks successfully removed! Elements removed: {total_removed} (images: {images_removed}, links: {links_removed})'

                # Return processed file
                return FileResponse(
                    output_path,
                    media_type='application/pdf',
                    filename=output_filename,
                    headers={"Content-Disposition": f"attachment; filename={output_filename}"}
                )
            else:
                success_message = 'Gamma.app watermarks not found in PDF.'
                return templates.TemplateResponse(
                    "index.html",
                    {"request": request, "success_message": success_message}
                )

        except Exception as e:
            error_message = f'Error processing file: {str(e)}'
            print(f"Error: {error_message}")
            return templates.TemplateResponse(
                "index.html",
                {"request": request, "error_message": error_message}
            )
        finally:
            # Remove temporary file
            try:
                os.unlink(upload_path)
            except:
                pass

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    """HTTP error handler"""
    if exc.status_code == 404:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "error_message": "Page not found."},
            status_code=404
        )
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "error_message": f"Server error: {exc.detail}"},
        status_code=exc.status_code
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """General error handler"""
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "error_message": f"Internal server error: {str(exc)}"},
        status_code=500
    )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
