import graphene 
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from .models import User

from .serializers import UserSerializer


# # User Type Configuration
class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'
        convert_choices_to_enums = ['language', 'country']


# Query Definition
class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.ID())

    def resolve_users(root, info, **kwargs):
        return User.objects.all()

    def resolve_user(root, info, id):
        return User.objects.get(pk=id)


# # Mutation Configuration

# # User Input - Create User
# class UserInput(graphene.InputObjectType):
#     username = graphene.String(required=False)
#     real_name = graphene.String(required=False)
#     bio = graphene.String(required=False)


# class CreateUser(graphene.Mutation):
#     class Arguments:
#         input = UserInput(required=True)

#     user = graphene.Field(UserType)

#     @classmethod
#     def mutate(cls, root, info, input):
#         user = User()
#         user.username = input.username
#         user.real_name = input.real_name
#         user.bio = input.bio
#         user.save()
#         return CreateUser(user=user)

# # class SignPledge(graphene.Mutation):
# #     class Arguments:
# #         id = graphene.ID()


class UserMutation(SerializerMutation):
    class Meta:
        serializer_class = UserSerializer
        model_operations = ['create', 'update']
        
        


# # Mutation Definition

class Mutation(graphene.ObjectType):
    userEdit = UserMutation().Field()

    
# class UpdateUser(graphene.Mutation):
#     class Arguments:
#         id = graphene.ID()
#         name = graphene.String(required=True)

#     user = graphene.Field(UserType)

#     @classmethod
#     def mutate(cls, root, info, title, id)

schema = graphene.Schema(query=Query, mutation=Mutation)