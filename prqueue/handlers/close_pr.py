import services
from typing import Any, Dict

def close_pr(data: Dict[str, Any]) -> str:
    
    link = data.get('link', None)
    if link is None:
        raise Exception('no link to pull request provided')
    
    try:
        if services.close_pr(link):
            return {'status': 200}
        else:
            return {'error': f'Pull request "{link}" does not exist'}
    except Exception as e:
        raise Exception from e