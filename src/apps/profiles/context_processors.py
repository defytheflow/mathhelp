from .apps import ProfilesConfig as profiles_config


def profiles(request):
    return {
        'PROFILE_DETAIL_URL': profiles_config.PROFILE_DETAIL_URL,
        'PROFILE_UPDATE_URL': profiles_config.PROFILE_UPDATE_URL,
    }