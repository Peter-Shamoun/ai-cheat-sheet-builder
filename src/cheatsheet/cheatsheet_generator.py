import os
from typing import List
from jinja2 import Environment, FileSystemLoader

class CheatSheetGenerator:
    def __init__(self, template_dir: str, output_dir: str):
        """
        Initializes the CheatSheetGenerator with directories for templates and output.

        Args:
            template_dir (str): Directory where the cheat sheet templates are stored.
            output_dir (str): Directory where the generated cheat sheets will be saved.
        """
        self.template_dir = template_dir
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

        self.env = Environment(loader=FileSystemLoader(self.template_dir))

    def generate_cheat_sheet(self, sections: List[str], output_name: str):
        """
        Generates a cheat sheet from the provided sections and saves it as a PDF.

        Args:
            sections (List[str]): The content sections to include in the cheat sheet.
            output_name (str): The name of the output cheat sheet file.
        """
        try:
            template = self.env.get_template("cheatsheet_template.tex")

            # Render the template with the sections
            rendered_content = template.render(sections=sections)

            # Write the rendered content to a .tex file
            tex_file_path = os.path.join(self.output_dir, f"{output_name}.tex")
            with open(tex_file_path, "w") as tex_file:
                tex_file.write(rendered_content)

            # Compile the .tex file to PDF
            pdf_output_path = os.path.join(self.output_dir, f"{output_name}.pdf")
            os.system(f"pdflatex -output-directory={self.output_dir} {tex_file_path}")

            return pdf_output_path

        except Exception as e:
            raise RuntimeError(f"Failed to generate cheat sheet: {str(e)}")
