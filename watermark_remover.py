import fitz
class WatermarkRemover:
    def remove_watermarks(self, pdf_path, images_to_remove_info, output_pdf_path="output_without_watermarks.pdf"):
        try:
            pdf_document = fitz.open(pdf_path)
            removed_count = 0
            removed_links = 0
            for image_info in reversed(images_to_remove_info):
                page_num = image_info['page']
                xref = image_info['xref']
                page_to_modify = pdf_document[page_num]
                try:
                    page_to_modify.delete_image(xref)
                    removed_count += 1
                    print(f"Removed watermark image xref:{xref} (name '{image_info['image_name']}') from page {page_num + 1}.")
                    
                    # Remove Gamma watermark links
                    links = page_to_modify.get_links()
                    for link in links:
                        uri = link.get("uri", "")
                        if "gamma.app" in uri:
                            page_to_modify.delete_link(link)
                            removed_links += 1
                            print(f"Removed Gamma watermark link '{uri}' from page {page_num + 1}")
                            
                except Exception as remove_error:
                    print(f"Error processing page {page_num + 1}: {remove_error}")
                    
            pdf_document.save(output_pdf_path)
            pdf_document.close()
            print(f"\nNew PDF without watermarks saved as: {output_pdf_path}")
            print(f"Total watermarks removed: {removed_count}")
            return output_pdf_path, None
            
        except Exception as e:
            return None, f"Error removing watermarks and saving PDF: {str(e)}"
