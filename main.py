from fastapi import FastAPI
from utils.logger import get_logger
from fastapi.staticfiles import StaticFiles
from models.home_response import HomeResponse
from models.description_response import DescriptionResponse
from models.description_request import DescriptionRequest
from models.ai_model_input import AIModelInput
from utils.methods import generate_id
from ai.gemini import generate_description

app = FastAPI()
logger = get_logger(name="API Logger")


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_model=HomeResponse)
async def home():
    logger.info(msg="Requested Home Page")
    return HomeResponse(message="Hello World!")


@app.post(
    "/create",
    response_model=DescriptionResponse,
    description="hello this is some description",
)
async def description(product: DescriptionRequest):
    product_dict = product.model_dump()
    ai_input_dict = AIModelInput(**product_dict)

    description_res = generate_description(ai_input_dict.model_dump())
    print(f"Description length: {len(description_res)}")

    id = generate_id()
    product_dict["id"] = id

    name = product_dict.pop("name", None)

    if name:
        product_dict["title"] = name

    if "images" in product_dict and type(product_dict["images"]) is list:
        product_dict["imageUrl"] = product_dict["images"][0]

    if "description" in product_dict and type(product_dict["description"]) is list:
        product_dict["description"] = description_res

    return DescriptionResponse(**product_dict)
