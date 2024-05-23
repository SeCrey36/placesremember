def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'vk-oauth2':
        user.vk_id = response.get('user_id')
        user.avatar_url = response.get('photo_max')
        user.save()
