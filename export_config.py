import os

print("Exporting WebSphere Full Configuration...")

# Define export directory
export_dir = "/tmp/ws_config_export"
if not os.path.exists(export_dir):
    os.makedirs(export_dir)

# Export Full WebSphere Profile
profile_export = os.path.join(export_dir, "was_profile.zip")
AdminTask.exportWasprofile('-archive ' + profile_export + ' -profileName AppSrv01')
print(f"Profile exported to {profile_export}")

# Export All Applications
apps = AdminApp.list().splitlines()
for app in apps:
    app_export = os.path.join(export_dir, f"{app}.ear")
    AdminApp.export(app, app_export)
    print(f"Application {app} exported to {app_export}")

# Export Data Sources
data_sources = AdminConfig.list('DataSource').splitlines()
for ds in data_sources:
    ds_name = AdminConfig.showAttribute(ds, 'name')
    ds_file = os.path.join(export_dir, f"ds_{ds_name}.txt")
    with open(ds_file, 'w') as f:
        f.write(AdminConfig.show(ds))
    print(f"DataSource {ds_name} configuration exported to {ds_file}")

# Export Security Settings
security_file = os.path.join(export_dir, "security_config.txt")
with open(security_file, 'w') as f:
    f.write(AdminConfig.show(AdminConfig.list('Security')))
print(f"Security settings exported to {security_file}")

# Export JVM Custom Properties
jvm_file = os.path.join(export_dir, "jvm_custom_properties.txt")
jvm_config = AdminConfig.list('JavaVirtualMachine')
with open(jvm_file, 'w') as f:
    f.write(AdminConfig.show(jvm_config))
print(f"JVM settings exported to {jvm_file}")

# Export Environment Variables
env_vars_file = os.path.join(export_dir, "environment_variables.txt")
env_vars = AdminConfig.list('VariableMap')
with open(env_vars_file, 'w') as f:
    f.write(AdminConfig.show(env_vars))
print(f"Environment variables exported to {env_vars_file}")

print("All configurations exported successfully!")
