import PyPDF2

class Resume:
    def __init__(self, file):
        self.file = file
        self.text = self.extract_text()

    def extract_text(self):
        text = ""
        try:
            reader = PyPDF2.PdfReader(self.file)
            for page in reader.pages:
                content = page.extract_text()
                if content:
                    text += content
        except:
            return "error"

        return text.lower()