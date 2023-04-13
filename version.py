# -*- coding: utf-8 -*-

class AppVersion:
    APP_VERSION = '1.0.0'
    APP_BUILD = '209'
    APP_BUILD_DATE = '2023-03-07'

    @staticmethod
    def get_version():
        return 'Version: ' + AppVersion.APP_VERSION

    @staticmethod
    def get_build():
        return 'Build: ' + AppVersion.APP_BUILD + ', ' + AppVersion.APP_BUILD_DATE