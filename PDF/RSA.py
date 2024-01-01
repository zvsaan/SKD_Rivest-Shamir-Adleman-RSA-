#!/usr/bin/env python
# coding: utf-8

# In[2]:


from PyPDF2 import PdfWriter, PdfReader

# Define input and output file paths
input_file_path = r"C:/Users/LENOVO/Downloads/File.pdf"
output_file_path = r"C:/Users/LENOVO/Downloads/Hasil.pdf"

try:
    # Open the original PDF file
    with open(input_file_path, "rb") as file:
        pdf = PdfReader(file)
        num = len(pdf.pages)

        # Create a PdfWriter object
        writer = PdfWriter()

        # Program reads each page of the file according to the identified pages
        for idx in range(num):
            writer.add_page(pdf.pages[idx])

        # Input the encryption password
        password = "tugasRSA"

        # Encrypt the output PDF
        writer.encrypt(user_pwd=password, use_128bit=True)

        # Output the encrypted file
        with open(output_file_path, "wb") as encrypted_file:
            writer.write(encrypted_file)

    print(f"Encryption successful. Encrypted file saved to {output_file_path}")

except Exception as e:
    print(f"An error occurred: {str(e)}")


# In[ ]:




