"""
Describe an image using a model.
"""

import ollama

# model_name = "llama3.2-vision"
model_name = "llava:34b"


def describe_image(image_path):
    """Describe an image using the specified model."""
    try:
        # Send the message to the model
        response = ollama.chat(
            model="llama3.2-vision",
            messages=[
                {
                    "role": "user",
                    "content": "Describe this image factually in extreme detail, less information is better than uncertain information, do not say anything unless sure, I do not see and I count on you.",
                    "images": [image_path],
                }
            ],
        )

        # Return the model's response
        return response["message"]["content"]

    except Exception as e:
        raise Exception(f"Error: {str(e)}")


# Example usage
if __name__ == "__main__":
    image_path = "/Users/roland/code/file_extractor/content/source/the_image.png"  # Replace with your image path
    try:
        description = describe_image(image_path)
        print("Image Description:")
        print(description)
    except Exception as e:
        print(f"Error: {str(e)}")
