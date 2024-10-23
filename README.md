# FastAPI Replicate Image Generation

This FastAPI application uses the [Replicate API](https://replicate.com/) to generate images based on text prompts and fine-tuning.

## Features

- Generate images using a prompt with customizable width, height, and number of images.
- Fine-tune a model using a dataset.
- Secure sensitive data using environment variables.
  
## Prerequisites

- Python 3.8+
- A Replicate account and API token

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/Fine_tune-Regenerate_Images.git
   cd Fine_tune-Regenerate_Images
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the root of your project:**

   ```bash
   touch .env
   ```

   Inside the `.env` file, add your Replicate API token:

   ```env
   REPLICATE_API_TOKEN=your_replicate_api_token
   ```

   Replace `your_replicate_api_token` with your actual API token from Replicate.

## Usage

1. **Run the FastAPI server:**

   ```bash
   uvicorn main:app --reload
   ```

   This will start the server on `http://127.0.0.1:8000`.

2. **Access the API Documentation:**

   Open the following link in your browser to see the interactive API documentation:

   - [FastAPI Docs](http://127.0.0.1:8000/docs)

3. **Generate Images:**

   Use the `/generate-images/` endpoint to generate images. Here’s an example of a request body:

   ```json
   {
     "prompt": "A futuristic cityscape at night",
     "width": 512,
     "height": 512,
     "num_images": 1
   }
   ```

   This will generate images based on the provided prompt.

## Project Structure

```
.
├── main.py               # FastAPI application code
├── .env                  # Environment variables (not tracked by Git)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Environment Variables

- `REPLICATE_API_TOKEN`: Your API token for authenticating requests to Replicate.

## Example Request

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/generate-images/' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "A beautiful mountain landscape",
  "width": 512,
  "height": 512,
  "num_images": 1
}'
```

## Dependencies

All required dependencies are listed in the `requirements.txt` file:

```txt
fastapi==0.95.1
uvicorn==0.22.0
requests==2.28.1
python-dotenv==1.0.0
```

To install them, run:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License.

## Acknowledgments

- Thanks to [Replicate](https://replicate.com/) for providing the API for image generation.
- FastAPI for the API framework.

---

This should provide a clear overview for users who wish to clone, set up, and run your project!