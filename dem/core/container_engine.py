"""Docker container engine management."""
# dem/core/container_engine.py

import docker

class ContainerEngine():
    def __init__(self) -> None:
        """Operations on the Docker Container Engine."""
        self._docker_client = docker.from_env()

    def get_local_tool_images(self) -> list[str]:
        """Get local tool images.
        
        Return with the list of the locally avialable tool image names.
        """
        local_image_tags = []

        for image in self._docker_client.images.list():
            for tag in image.tags:
                if tag and tag.startswith("axemsolutions/"):
                    local_image_tags.append(tag)

        return local_image_tags

    def pull(self, repository: str) -> None:
        """Pull a repository from the axemsolutions registry.
        
        Args:
            repository -- repository to pull"""
        self._docker_client.images.pull(repository=repository)