from rest_framework import serializers
from users.models import Article, UserAccount

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'user','title', 'text', 'rating', 'date']
        # read_only_fields = ['user', 'date']
        
    # def create(self, validated_data):
    #     print(validated_data)
    #     user_id = validated_data.pop('user')  # Extract user_id from validated data
    #     user = UserAccount.objects.get(pk=user_id)  # Retrieve user instance using user_id
    #     article = Article.objects.create(user=user, **validated_data)  # Create article with associated user
    #     return article