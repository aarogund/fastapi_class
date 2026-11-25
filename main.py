from fastapi import FastAPI, HTTPException
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FASTAPI class"}

@app.get("/health")
def read_health():
    return {"health status": "Healthy"}

@app.get("/books")
def read_books():
    return {"books":["Riyad as-Salihin", "Sahih Bukhari", "Sahih Muslim", "Tafseer by Ibn Kathir"]}

@app.get("/books/{book_title}")
def read_book(book_title:str):
    books = {
        "Ibn Kathir": {"description": "A notable tafsir(exegesis) of the Quran", "Author": "Ibn Kathir", "year": "1301-1373 CE"},
        "Riyad as-Salihin": {"description": " A compilation of hadiths by Imam Nawawi, focusing on ethics and morals.", "Author": "Imam Nawawi", "year": "1272 CE"},
        "Sahih al-Bukhari": {"description": "One of the most authentic collections of hadiths compiled by Imam Bukhari.", "Author": "Imam Bukhari", "year": "846 CE"},
        "Sahih Muslim": {"description": "A highly regarded collection of hadiths compiled by Imam Muslim.", "Author": "Imam Muslim", "year": "864-875 CE"}      
    }

    if book_title in books:
        return {"title": book_title, "description": books[book_title]["description"], "Author": books[book_title]["Author"], "Year": books[book_title]["year"]}
    else:
        raise HTTPException(status_code=404, detail="Book not found")
