import fitz
import re
import os

class PDFProcessor:
    def __init__(self, target_domain="gamma.app", corner_threshold=0.7):
        self.target_domain = target_domain
        self.corner_threshold = corner_threshold

    def clean_pdf(self, input_path: str, output_path: str) -> (int, int):
        if not os.path.exists(os.path.dirname(output_path)):
            os.makedirs(os.path.dirname(output_path))

        doc = fitz.open(input_path)
        total_images_removed = 0
        total_links_removed = 0

        for page_num, page in enumerate(doc):
            images_removed, links_removed = self._process_page(page)
            total_images_removed += images_removed
            total_links_removed += links_removed

        doc.save(output_path)
        doc.close()
        return total_images_removed, total_links_removed

    def _process_page(self, page: fitz.Page) -> (int, int):
        images_removed = self._remove_corner_images(page)
        links_removed = self._remove_all_target_links(page)
        return images_removed, links_removed

    def _remove_corner_images(self, page: fitz.Page) -> int:
        page_rect = page.rect
        right_threshold = page_rect.width * self.corner_threshold
        bottom_threshold = page_rect.height * self.corner_threshold
        
        images_to_remove = {
            xref
            for img in page.get_images(full=True)
            for xref in [img[0]]
            for img_rect in page.get_image_rects(xref)
            if self._is_in_corner(img_rect, right_threshold, bottom_threshold)
            and self._has_target_link(img_rect, page)
        }

        for xref in images_to_remove:
            page.delete_image(xref)
        return len(images_to_remove)

    def _is_in_corner(self, rect: fitz.Rect, right_threshold: float, bottom_threshold: float) -> bool:
        return rect.x0 >= right_threshold and rect.y0 >= bottom_threshold

    def _has_target_link(self, obj_rect: fitz.Rect, page: fitz.Page) -> bool:
        return any(
            obj_rect.intersects(fitz.Rect(link['from'])) and self.target_domain in link.get('uri', '').lower()
            for link in page.get_links()
        )

    def _remove_all_target_links(self, page: fitz.Page) -> int:
        links_to_remove = [
            link for link in page.get_links() if self.target_domain in link.get('uri', '').lower()
        ]
        for link in links_to_remove:
            page.delete_link(link)
        return len(links_to_remove)

def secure_filename(filename: str) -> str:
    _windows_device_files = (
        "CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5",
        "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2", "LPT3", "LPT4",
        "LPT5", "LPT6", "LPT7", "LPT8", "LPT9",
    )
    assert filename, "filename must not be empty"
    
    if os.name == "nt" and filename.split(".")[0].upper() in _windows_device_files:
        return "_" + filename
        
    return re.sub(r"[\/:*?\"<>|]", "_", filename)