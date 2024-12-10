import os
import webbrowser
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import Spacer
from datetime import datetime
import tempfile


def generate_pdf_and_open(data, database_name):
    """
    Generates a temporary PDF file with a formatted table of book details and opens it for the user.
    The user can choose to save it manually or simply close the viewer.

    :param data: List of tuples representing rows from the database.
                 Each tuple should contain (Title, Author, Genre, Published Date).
    :param database_name: Name of the database for the header.
    """
    # Create a temporary file
    temp_dir = tempfile.gettempdir()
    temp_file = os.path.join(temp_dir, "library_report.pdf")

    # Define PDF document and styles
    doc = SimpleDocTemplate(temp_file, pagesize=landscape(letter))
    styles = getSampleStyleSheet()
    elements = []

    # Add header
    header_text = f"{database_name.capitalize()}'s Library (Generated on {datetime.now().strftime('%Y-%m-%d')})"
    header = Paragraph(header_text, styles['Title'])
    elements.append(header)
    elements.append(Spacer(1, 12))  # Add spacing below header

    # Add table data
    table_data = [["Title", "Author", "Genre", "Published Date"]]  # Table header
    for row in data:
        table_data.append(list(row))  # Convert tuple to list and add to table

    # Set column widths and wrap text
    col_widths = [200, 150, 100, 120]  # Adjust widths as needed
    wrapped_table_data = [[Paragraph(str(cell), styles['Normal']) for cell in row] for row in table_data]

    # Create table and style it
    table = Table(wrapped_table_data, colWidths=col_widths)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.whitesmoke, colors.lightgrey]),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    elements.append(table)

    # Build PDF
    doc.build(elements)

    # Open the PDF in the default viewer
    webbrowser.open(f"file://{temp_file}")

    print("PDF opened in your default viewer. Save manually if desired.")
