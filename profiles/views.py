from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from django.http import Http404
from .models import Profile
from .serializers import ProfileSerializer, UserProfileSerializer

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_queryset(self):
        queryset = Profile.objects.all()
        username = self.request.query_params.get('search', None)
        if username is not None:
            queryset = queryset.filter(user__username__icontains=username)
        return queryset

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(user=user)

    def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        if self.request.method == 'GET':
            follow_url = reverse('follow', kwargs={'username': context['view'].get_object().user.username})
            unfollow_url = reverse('unfollow', kwargs={'following_id': context['view'].get_object().user.id})
            response.context_data['follow_url'] = follow_url
            response.context_data['unfollow_url'] = unfollow_url
        return response

class UserProfileViewByUsername(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'username'

    def get_object(self):
        username = self.kwargs.get('username')
        try:
            return Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise Http404