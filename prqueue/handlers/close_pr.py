import services
import exceptions
from typing import Any, Dict

def close_pr(data: Dict[str, Any]) -> str:
    
    link = data.get('link', None)
    if link is None:
        raise exceptions.MissingLinkException()
    
    return services.close_pr(link)
