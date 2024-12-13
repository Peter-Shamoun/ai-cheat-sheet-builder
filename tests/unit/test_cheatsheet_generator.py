import os
import pytest
from cheatsheet.cheatsheet_generator import CheatSheetGenerator

def test_generate_cheat_sheet():
    """
    Test that the CheatSheetGenerator correctly generates a LaTeX file and compiles it to a PDF.
    """
    template_dir = "./src/cheatsheet/templates"  # Use the absolute or relative path to the template directory
    output_dir = "./data/test_output"
    os.makedirs(output_dir, exist_ok=True)

    generator = CheatSheetGenerator(template_dir=template_dir, output_dir=output_dir)

    # Mock sections to populate the template
    sections = ["Introduction", "Key Concepts", "Summary"]

    # Generate the cheat sheet
    output_name = "test_cheatsheet"
    pdf_path = generator.generate_cheat_sheet(sections=sections, output_name=output_name)

    # Assertions
    assert os.path.exists(pdf_path)

    # Cleanup
    os.remove(os.path.join(output_dir, f"{output_name}.tex"))
    os.remove(pdf_path)
    os.rmdir(output_dir)
