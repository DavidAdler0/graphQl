import graphene

from graphene_sqlalchemy import  SQLAlchemyObjectType
from database import db_session
from models import MissionModel, CountryModel, CityModel, TargetTypesModel, TargetModel


# class User(SQLAlchemyObjectType):
#     class Meta:
#         model = UserModel
#         interfaces = (graphene.relay.Node,)
# class Subject(SQLAlchemyObjectType):
#     class Meta:
#         model = SubjectModel
#         interfaces = (graphene.relay.Node,)

class Mission(SQLAlchemyObjectType):
    class Meta:
        model = MissionModel
        interfaces = (graphene.relay.Node,)
class Country(SQLAlchemyObjectType):
    class Meta:
        model = CountryModel
        interfaces = (graphene.relay.Node,)
class City(SQLAlchemyObjectType):
    class Meta:
        model = CityModel
        interfaces = (graphene.relay.Node,)
class TargetTypes(SQLAlchemyObjectType):
    class Meta:
        model = TargetTypesModel
        interfaces = (graphene.relay.Node,)
class Target(SQLAlchemyObjectType):
    class Meta:
        model = TargetModel
        interfaces = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    mission_by_id = graphene.Field(Mission, mission_id=graphene.Int(required=True))
    missions_by_date_range = graphene.List(Mission, min_date=graphene.Date(required=True), max_date=graphene.Date(required=True))
    mission_by_target_industry = graphene.List(Mission, target_industry=graphene.String(required=True))

    mission_results_by_target_type = graphene.Field(Mission, target_type=graphene.String(required=True))
    @staticmethod
    def resolve_mission_by_id(self, info, mission_id):
        return db_session.query(MissionModel).get(mission_id)

    @staticmethod
    def resolve_missions_by_date_range(root, info, min_date, max_date):
        return db_session.query(MissionModel).filter(MissionModel.mission_date.between(min_date, max_date))
    @staticmethod
    def resolve_missions_by_target_industry(self, info, target_industry):
        return db_session.query(MissionModel).join(MissionModel.targets).filter(TargetModel.target_industry == target_industry).all()


    # def resolve_users_by_name(self, info, name_substring):
    #     substring = f"%{name_substring}%"
    #     return db_session.query(UserModel).filter(UserModel.first_name.ilike(substring)).all()
    # def resolve_users_by_subject(self, info, subject_id):
    #     return db_session.query(UserModel).join(UserModel.subjects).filter(UserModel.subject_id == subject_id).all()

schema = graphene.Schema(query=Query)