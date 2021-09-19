import graphene 
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from .models import Pledge, Action

from .serializers import ActionSerializer, PledgeSerializer, UpdatePledgeSerializer, UpdateActionSerializer

class ActionStepType(DjangoObjectType):
    class Meta:
        model = Action
        fields = '__all__'
        convert_choices_to_enum = ['frequency']

class PledgeType(DjangoObjectType):
    class Meta:
        model = Pledge
        fields = '__all__'

class Query(graphene.ObjectType):
    pledges = graphene.List(PledgeType)
    actions = graphene.List(ActionStepType)
    pledge = graphene.Field(PledgeType, id=graphene.ID())
    action = graphene.Field(ActionStepType, id=graphene.ID())
    

    def resolve_pledge(root, info, id):
        return Pledge.objects.get(pk=id)

    def resolve_action(root, info, id):
        return Action.objects.get(pk=id)

    def resolve_pledges(root, info, **kwargs):
        return Pledge.objects.all()
    
    def resolve_actions(root, info, **kwargs):
        return Action.objects.all()


class ActionStepMutation(SerializerMutation):
    class Meta:
        serializer_class = ActionSerializer
        model_operations = ['create']
        


class PledgeMutation(SerializerMutation):
    class Meta:
        serializer_class = PledgeSerializer
        model_operations = ['create']
       
class UpdatePledgeMutation(SerializerMutation):
    class Meta:
        serializer_class = UpdatePledgeSerializer
        model_operations = ['update']

class UpdateActionMutation(SerializerMutation):
    class Meta:
        serializer_class = UpdateActionSerializer
        model_operations = ['update']

class Mutation(graphene.ObjectType):
    createAction = ActionStepMutation().Field()
    updateAction = UpdateActionMutation().Field()
    createPledge = PledgeMutation().Field()
    updatePledge = UpdatePledgeMutation().Field()


schema = graphene.Schema(query=Query, mutation=Mutation)


# class PledgeInput(graphene.InputObjectType):
#     mission = graphene.String(required=True)
#     impact_statement = graphene.String(required=True)
    
# class CreatePledge(graphene.Mutation):
#     class Arguments:
#         pledge_data = PledgeInput(required=True)
#         author_id = graphene.ID()

#     pledge = graphene.Field(PledgeType)

#     @classmethod
#     def mutate(cls, root, info, pledge_data, author_id):
#         user = User.objects.get(pk=author_id)
#         pledge = Pledge()
#         pledge.mission = pledge_data.mission
#         pledge.impact_statement = pledge_data.impact_statement
#         pledge.author = user
#         pledge.save()
#         return CreatePledge(pledge = pledge)

# class ActionStepInput(graphene.InputObjectType):
#     title = graphene.String(required=True)
#     unit_type = graphene.String(required=True)
#     unit_amount = graphene.Int(required=True)
#     frequency = graphene.String(required=True)

# class CreateActionStep(graphene.Mutation):
#     class Arguments:
#         data = ActionStepInput(required=True)
#         pledge = graphene.ID()

#     action_step = graphene.Field(ActionStepType)

#     @classmethod
#     def mutate(cls, root, info, data, pledge_id):
#         pledge = Pledge.objects.get(pk=pledge_id)
#         ac = Action()
#         ac.title = data.title
#         ac.unit_type = data.unit_type
#         ac.unit_amount = data.unit_amount
#         ac.frequency = data.frequency
#         ac.save()
#         return CreateActionStep(ac=ac)

# class Mutation(graphene.ObjectType):
#     create_action_step = CreateActionStep.Field()
#     create_pledge = CreatePledge.Field()

# schema = graphene.Schema(query=Query, mutation=Mutation)