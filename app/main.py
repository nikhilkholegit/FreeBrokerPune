from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .repository import repository


BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(title="Pune Rent Connect")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
def home(request: Request, area: str = "All", q: str = "") -> HTMLResponse:
    listings = repository.all(area=area, query=q)
    context = {
        "request": request,
        "listings": listings,
        "areas": repository.areas(),
        "selected_area": area,
        "query": q,
        "featured_count": len(listings),
    }
    return templates.TemplateResponse("index.html", context)


@app.get("/listings/{listing_id}", response_class=HTMLResponse)
def listing_detail(request: Request, listing_id: int) -> HTMLResponse:
    listing = repository.get(listing_id)
    if listing is None:
        return templates.TemplateResponse(
            "not_found.html",
            {"request": request, "message": "That property could not be found."},
            status_code=404,
        )
    return templates.TemplateResponse(
        "detail.html",
        {"request": request, "listing": listing},
    )


@app.get("/post", response_class=HTMLResponse)
def post_form(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "post.html",
        {"request": request, "areas": repository.areas()[1:], "errors": [], "values": {}},
    )


@app.post("/post")
def create_listing(
    request: Request,
    title: str = Form(...),
    area: str = Form(...),
    rent: int = Form(...),
    deposit: int = Form(...),
    bhk: str = Form(...),
    furnishing: str = Form(...),
    available_from: str = Form(...),
    description: str = Form(...),
    owner_name: str = Form(...),
    phone: str = Form(...),
):
    errors = []
    values = {
        "title": title,
        "area": area,
        "rent": rent,
        "deposit": deposit,
        "bhk": bhk,
        "furnishing": furnishing,
        "available_from": available_from,
        "description": description,
        "owner_name": owner_name,
        "phone": phone,
    }

    if len(phone.strip()) < 10:
        errors.append("Phone number must have at least 10 digits.")
    if rent <= 0:
        errors.append("Rent must be greater than zero.")
    if deposit < 0:
        errors.append("Deposit cannot be negative.")

    if errors:
        return templates.TemplateResponse(
            "post.html",
            {"request": request, "areas": repository.areas()[1:], "errors": errors, "values": values},
            status_code=400,
        )

    listing = repository.create(
        title=title.strip(),
        area=area.strip(),
        rent=rent,
        deposit=deposit,
        bhk=bhk.strip(),
        furnishing=furnishing.strip(),
        available_from=available_from.strip(),
        description=description.strip(),
        owner_name=owner_name.strip(),
        phone=phone.strip(),
    )
    return RedirectResponse(url=f"/listings/{listing.id}", status_code=303)
