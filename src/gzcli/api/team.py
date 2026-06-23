from gzcli.api._http import APIProfile, make_post
from gzcli.api.models.info import TeamUpdateModel, TeamInfoModel


def create_team(profile: APIProfile, body: TeamUpdateModel) -> TeamInfoModel:
    """
    API wrapper for `/api/team`
    docs: https://gzctf.gzti.me/scalar.html#tag/team/POST/api/team
    """
    resp = make_post(
        profile,
        "/api/team",
        json=body.model_dump(exclude_none=True),
    )
    return TeamInfoModel.model_validate(resp.json())
