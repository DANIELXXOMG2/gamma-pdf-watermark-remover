import fitz
from PIL import Image
import io
import numpy as np
from config import WatermarkConfig

class WatermarkDetector:
    def __init__(self, template_histogram=None, similarity_threshold=WatermarkConfig.SIMILARITY_THRESHOLD):
        self.template_histogram = template_histogram if template_histogram else WatermarkConfig.get_template_histogram_array()
        self.similarity_threshold = similarity_threshold

    def calculate_histogram(self, image_data):
        img = Image.open(io.BytesIO(image_data)).convert('L')
        hist, _ = np.histogram(img, bins=256, range=(0, 256))
        return hist / np.sum(hist)

    def compare_histograms(self, hist1, hist2):
        intersection = np.minimum(hist1, hist2).sum()
        similarity = intersection / np.sum(hist1)
        return similarity

    def identify_watermarks(self, pdf_path):
        images_to_remove_info = []
        try:
            pdf_document = fitz.open(pdf_path)
            print("\nSearching for watermarks...\n")
            for page_num in range(pdf_document.page_count):
                page = pdf_document[page_num]
                image_list = page.get_images(full=True)

                for img_info_tuple in image_list:
                    xref = img_info_tuple[0]
                    img_index = img_info_tuple[1]

                    try:
                        base_image = pdf_document.extract_image(xref)
                        image_bytes = base_image["image"]
                        if image_bytes:
                            current_hist = self.calculate_histogram(image_bytes)
                            similarity = self.compare_histograms(self.template_histogram, current_hist)

                            print(f"  Similarity of image xref:{xref} on page {page_num + 1}: {similarity * 100:.2f}%")

                            if similarity >= self.similarity_threshold:
                                image_name = f"Image_{img_index}.{base_image['ext']}"
                                images_to_remove_info.append({
                                    'page': page_num,
                                    'xref': xref,
                                    'image_name': image_name,
                                    'similarity': similarity
                                })
                                print(f"Watermark candidate found on page {page_num + 1}:")
                                print(f"  Image name: {image_name}, xref: {xref}")
                                print(f"  Similarity to watermark template: {similarity * 100:.2f}%")
                                print("-" * 50)
                        else:
                            print(f"  - Error: Could not get image bytes for xref {xref} on page {page_num + 1}.")

                    except Exception as inner_e:
                        print(f"Error processing image xref {xref} on page {page_num + 1}: {inner_e}")

            pdf_document.close()

            if not images_to_remove_info:
                print(f"No watermarks found with threshold {self.similarity_threshold * 100:.0f}% in PDF.")
            return images_to_remove_info, None

        except Exception as e:
            return [], f"Error identifying watermarks: {str(e)}"