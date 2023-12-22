import os
def save_uploaded_file(uploaded_file):
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        # Then save the buffer to a file.
        with open(uploaded_file.name, "wb") as f:
            f.write(bytes_data)
        return uploaded_file.name

    return None
