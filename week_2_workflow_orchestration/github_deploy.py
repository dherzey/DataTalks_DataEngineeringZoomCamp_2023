from prefect_github.repository import GitHubRepository
from prefect.deployments import Deployment
from week_2_workflow_orchestration.parameterized_flow import etl_parent_flow

github_block = GitHubRepository.load("zoomcamp-github")
github_dep = Deployment.build_from_flow(
    flow = etl_parent_flow,
    name = "flow-github-storage",
    storage = github_block
)

if __name__=="__main__":
    github_dep.apply()