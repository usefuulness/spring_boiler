import subprocess
import os

def initialize_maven_project(group_id, artifact_id, version, archetype_artifact_id):
    # Set the Maven command to run
    maven_command = "mvn archetype:generate"

    # Define the Maven archetype parameters
    archetype_params = [
        f"-DgroupId={group_id}",
        f"-DartifactId={artifact_id}",
        f"-Dversion={version}",
        f"-DarchetypeArtifactId={archetype_artifact_id}",
        "-DinteractiveMode=false"
    ]

    # Execute the Maven command
    subprocess.run([maven_command] + archetype_params, check=True)

def main():
    # Gather Maven project information
    group_id = input("Enter the Group Id: ")
    artifact_id = input("Enter the Artifact Id: ")
    version = input("Enter the Version: ")
    archetype_artifact_id = input("Enter the Archetype Artifact Id: ")

    # Create a directory for the Maven project
    project_dir = f"{artifact_id}-maven-project"
    os.makedirs(project_dir, exist_ok=True)

    # Change to the project directory
    os.chdir(project_dir)

    # Initialize the Maven project
    initialize_maven_project(group_id, artifact_id, version, archetype_artifact_id)

    print(f"Maven project '{artifact_id}' initialized successfully in '{project_dir}'.")

if __name__ == "__main__":
    main()
