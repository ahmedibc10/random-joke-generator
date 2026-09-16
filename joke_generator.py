import requests
import random
from typing import Dict, List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class JokeGenerator:
    """فئة توليد النكات من واجهات برمجية مختلفة"""
    
    def __init__(self):
        """تهيئة مولد النكات"""
        self.apis = {
            'official_joke_api': 'https://official-joke-api.appspot.com',
            'jokes_api': 'https://v2.jokeapi.dev',
            'dad_jokes': 'https://icanhazdadjoke.com',
        }
    
    def get_random_joke_from_official_api(self) -> Dict:
        """
        الحصول على نكتة عشوائية من Official Joke API
        
        Returns:
            dict يحتوي على النكتة
        """
        try:
            url = f"{self.apis['official_joke_api']}/random_joke"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            logger.info("تم الحصول على نكتة من Official Joke API")
            return {
                'type': 'single',
                'setup': data.get('setup', ''),
                'punchline': data.get('punchline', ''),
                'source': 'Official Joke API',
                'id': data.get('id')
            }
        except Exception as e:
            logger.error(f"خطأ في Official Joke API: {e}")
            return {'error': str(e)}
    
    def get_random_joke_from_jokes_api(self, joke_type: str = 'any') -> Dict:
        """
        الحصول على نكتة من JokeAPI
        
        Args:
            joke_type: نوع النكتة (any, single, twopart)
            
        Returns:
            dict يحتوي على النكتة
        """
        try:
            url = f"{self.apis['jokes_api']}/joke/{joke_type}"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('error'):
                return {'error': 'لم يتم العثور على نكتة'}
            
            logger.info("تم الحصول على نكتة من JokeAPI")
            
            if data.get('type') == 'single':
                return {
                    'type': 'single',
                    'joke': data.get('joke', ''),
                    'source': 'JokeAPI',
                    'id': data.get('id')
                }
            else:
                return {
                    'type': 'twopart',
                    'setup': data.get('setup', ''),
                    'delivery': data.get('delivery', ''),
                    'source': 'JokeAPI',
                    'id': data.get('id')
                }
        except Exception as e:
            logger.error(f"خطأ في JokeAPI: {e}")
            return {'error': str(e)}
    
    def get_dad_joke(self) -> Dict:
        """
        الحصول على dad joke من icanhazdadjoke.com
        
        Returns:
            dict يحتوي على النكتة
        """
        try:
            url = self.apis['dad_jokes']
            headers = {'Accept': 'application/json'}
            response = requests.get(url, headers=headers, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            logger.info("تم الحصول على dad joke")
            return {
                'type': 'single',
                'joke': data.get('joke', ''),
                'source': 'icanhazdadjoke',
                'id': data.get('id')
            }
        except Exception as e:
            logger.error(f"خطأ في icanhazdadjoke: {e}")
            return {'error': str(e)}
    
    def get_random_joke(self) -> Dict:
        """
        الحصول على نكتة عشوائية من واحدة من الواجهات البرمجية
        
        Returns:
            dict يحتوي على النكتة
        """
        sources = [
            self.get_random_joke_from_official_api,
            self.get_random_joke_from_jokes_api,
            self.get_dad_joke
        ]
        
        selected_source = random.choice(sources)
        return selected_source()
    
    def get_multiple_jokes(self, count: int = 5) -> List[Dict]:
        """
        الحصول على عدة نكات
        
        Args:
            count: عدد النكات المطلوبة
            
        Returns:
            قائمة بالنكات
        """
        jokes = []
        for i in range(count):
            joke = self.get_random_joke()
            jokes.append(joke)
        return jokes
    
    def get_category_joke(self, category: str = 'Programming') -> Dict:
        """
        الحصول على نكتة من فئة محددة
        
        Args:
            category: الفئة المطلوبة
            
        Returns:
            dict يحتوي على النكتة
        """
        try:
            valid_categories = [
                'programming',
                'misc',
                'knock-knock',
                'general',
                'spooky',
                'dark'
            ]
            
            if category.lower() not in valid_categories:
                category = 'any'
            
            url = f"{self.apis['jokes_api']}/joke/{category}"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('error'):
                return {'error': 'لم يتم العثور على نكتة في هذه الفئة'}
            
            logger.info(f"تم الحصول على نكتة من فئة {category}")
            return data
        except Exception as e:
            logger.error(f"خطأ في الحصول على نكتة من فئة {category}: {e}")
            return {'error': str(e)}
