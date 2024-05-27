# main/pipeline.py
import logging

logger = logging.getLogger(__name__)

def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'vk-oauth2':
        logger.info(f"VK Response: {response}")
        
        vk_id = response.get('id')
        avatar_url = response.get('photo_max_orig')

        logger.info(f"VK ID: {vk_id}, Avatar URL: {avatar_url}")

        user.vk_id = vk_id
        user.avatar_url = avatar_url if avatar_url else user.avatar_url
        user.save()