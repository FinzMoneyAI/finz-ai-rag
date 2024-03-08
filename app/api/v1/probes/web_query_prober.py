from fastapi import APIRouter

probe_router = APIRouter(prefix="/probes", responses={ 404: { "description": "Not Found!"}})

@probe_router.get("/searchprobes")
def generate_search_probes(): 
    """
    Generate a list of search probes for the provided trail of hints. The clients should ideally build up a trail of hints 
    by multiple calls to thisPath operation.

    A search probe is something that can be used as search input on a search engine or web crawler.
    """
    probes = {
        "hint_trail": [], 
        "probes": []
    }
    
    return probes

