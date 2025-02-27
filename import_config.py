import os

print("Importing WebSphere Full Configuration...")

# Define import directory
import_dir = "/tmp/ws_config_export"

# Import WebSphere Profile
profile_import = os.path.join(import_dir, "was_profile.zip")
AdminTask.importWasprofile('-archive ' + profile_import + ' -profileName AppSrv01')
print(f"Profile imported from {profile_import}")

# Import Applications
for file in os.listdir(import_dir):
    if file.endswith(".ear"):
        app_import = os.path.join(import_dir, file)
        AdminApp.install(app_import, '[ -cell NewCell -node NewNode -server NewServer ]')
        print(f"Application {file} imported from {app_import}")

# Import Data Sources
for file in os.listdir(import_dir):
    if file.startswith("ds_") and file.endswith(".txt"):
        ds_file = os.path.join(import_dir, file)
        with open(ds_file, 'r') as f:
            ds_config = f.read()
        AdminConfig.create('DataSource', AdminConfig.list('Cell'), ds_config)
        print(f"DataSource imported from {ds_file}")

# Import Security Settings
security_file = os.path.join(import_dir, "security_config.txt")
with open(security_file, 'r') as f:
    security_config = f.read()
AdminConfig.create('Security', AdminConfig.list('Cell'), security_config)
print(f"Security settings imported from {security_file}")

# Import JVM Custom Properties
jvm_file = os.path.join(import_dir, "jvm_custom_properties.txt")
with open(jvm_file, 'r') as f:
    jvm_config = f.read()
AdminConfig.create('JavaVirtualMachine', AdminConfig.list('Server'), jvm_config)
print(f"JVM settings imported from {jvm_file}")

# Import Environment Variables
env_vars_file = os.path.join(import_dir, "environment_variables.txt")
with open(env_vars_file, 'r') as f:
    env_vars = f.read()
AdminConfig.create('VariableMap', AdminConfig.list('Cell'), env_vars)
print(f"Environment variables imported from {env_vars_file}")

AdminConfig.save()
print("All configurations imported successfully!")
