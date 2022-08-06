from rest_framework import generics
from .services import set_error_log, set_success_log
from rest_framework.renderers import JSONRenderer
import time


class LogCreateAPIView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):

        try:
            resp = super(LogCreateAPIView, self).post(request, *args, **kwargs)
            resp.accepted_renderer = JSONRenderer()
            resp.accepted_media_type = "application/json"
            resp.renderer_context = {}
            resp.render()
        except Exception as e:
            set_error_log(request, e)
            return e

        set_success_log(request, resp)
        return resp


class LogUpdateAPIView(generics.UpdateAPIView):
    def put(self, request, *args, **kwargs):
        # log request
        try:
            resp = super(LogUpdateAPIView, self).put(request, *args, **kwargs)
            resp.accepted_renderer = JSONRenderer()
            resp.accepted_media_type = "application/json"
            resp.renderer_context = {}
            resp.render()
        except Exception as e:
            set_error_log(request, e)
            return e
        set_success_log(request, resp)
        return resp

    def patch(self, request, *args, **kwargs):
        # log request
        try:
            resp = super(LogUpdateAPIView, self).patch(request, *args, **kwargs)
            resp.accepted_renderer = JSONRenderer()
            resp.accepted_media_type = "application/json"
            resp.renderer_context = {}
            resp.render()
        except Exception as e:
            set_error_log(request, e)
            return e
        set_success_log(request, resp)
        return resp


class LogDestroyAPIView(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        # log request
        try:
            resp = super(LogDestroyAPIView, self).delete(request, *args, **kwargs)
            resp.accepted_renderer = JSONRenderer()
            resp.accepted_media_type = "application/json"
            resp.renderer_context = {}
            resp.render()
        except Exception as e:
            set_error_log(request, e)
            return e
        set_success_log(request, resp)
        return resp


class LogRetrieveAPIView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        # log request
        try:
            resp = super(LogRetrieveAPIView, self).get(request, *args, **kwargs)
            resp.accepted_renderer = JSONRenderer()
            resp.accepted_media_type = "application/json"
            resp.renderer_context = {}
            resp.render()
        except Exception as e:
            set_error_log(request, e)
            return e
        set_success_log(request, resp)
        return resp


class LogListAPIView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        # log request
        try:
            resp = super(LogListAPIView, self).get(request, *args, **kwargs)
            resp.accepted_renderer = JSONRenderer()
            resp.accepted_media_type = "application/json"
            resp.renderer_context = {}
            resp.render()
        except Exception as e:
            set_error_log(request, e)
            return e
        set_success_log(request, resp)
        return resp


class LogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    def get(self, request, *args, **kwargs):
        # log request
        try:
            resp = super(LogRetrieveUpdateDestroyAPIView, self).get(request, *args, **kwargs)
            resp.accepted_renderer = JSONRenderer()
            resp.accepted_media_type = "application/json"
            resp.renderer_context = {}
            resp.render()
        except Exception as e:
            set_error_log(request, e)
            return e
        set_success_log(request, resp)
        return resp

    def put(self, request, *args, **kwargs):
        # log request
        try:
            resp = super(LogRetrieveUpdateDestroyAPIView, self).put(request, *args, **kwargs)
            resp.accepted_renderer = JSONRenderer()
            resp.accepted_media_type = "application/json"
            resp.renderer_context = {}
            resp.render()
        except Exception as e:
            set_error_log(request, e)
            return e
        set_success_log(request, resp)
        return resp

    def patch(self, request, *args, **kwargs):
        # log request
        try:
            resp = super(LogRetrieveUpdateDestroyAPIView, self).patch(request, *args, **kwargs)
            resp.accepted_renderer = JSONRenderer()
            resp.accepted_media_type = "application/json"
            resp.renderer_context = {}
            resp.render()
        except Exception as e:
            set_error_log(request, e)
            return e
        set_success_log(request, resp)
        return resp

    def delete(self, request, *args, **kwargs):
        # log request
        try:
            resp = super(LogRetrieveUpdateDestroyAPIView, self).delete(request, *args, **kwargs)
            resp.accepted_renderer = JSONRenderer()
            resp.accepted_media_type = "application/json"
            resp.renderer_context = {}
            resp.render()
        except Exception as e:
            set_error_log(request, e)
            return e
        set_success_log(request, resp)
        return resp


class LogRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    def get(self, request, *args, **kwargs):
        # log request
        try:
            resp = super(LogRetrieveUpdateAPIView, self).get(request, *args, **kwargs)
            resp.accepted_renderer = JSONRenderer()
            resp.accepted_media_type = "application/json"
            resp.renderer_context = {}
            resp.render()
        except Exception as e:
            set_error_log(request, e)
            return e
        set_success_log(request, resp)
        return resp

    def put(self, request, *args, **kwargs):
        # log request
        try:
            resp = super(LogRetrieveUpdateAPIView, self).put(request, *args, **kwargs)
            resp.accepted_renderer = JSONRenderer()
            resp.accepted_media_type = "application/json"
            resp.renderer_context = {}
            resp.render()
        except Exception as e:
            set_error_log(request, e)
            return e
        set_success_log(request, resp)
        return resp

    def patch(self, request, *args, **kwargs):
        # log request
        try:
            resp = super(LogRetrieveUpdateAPIView, self).patch(request, *args, **kwargs)
            resp.accepted_renderer = JSONRenderer()
            resp.accepted_media_type = "application/json"
            resp.renderer_context = {}
            resp.render()
        except Exception as e:
            set_error_log(request, e)
            return e
        set_success_log(request, resp)
        return resp
