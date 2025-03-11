---
description: 'Author: Allen'
---

# FAQ

## How to handle plugin upload failure during installation?

**Error Details**: The error message shows `PluginDaemonBadRequestError: plugin_unique_identifier is not valid`.

**Solution**: Modify the `author` field in both the `manifest.yaml` file in the plugin project and the `.yaml` file under the `/provider` path to your GitHub ID.

Retype the plugin packaging command and install the new plugin package.

## How to handle errors when installing plugins?

**Issue**: If you encounter the error message: `plugin verification has been enabled, and the plugin you want to install has a bad signature`, how to handle the issue?

**Solution**: Add the following line to the end of your `/docker/.env` configuration file: `FORCE_VERIFYING_SIGNATURE=false`. Run the following commands to restart the Dify service:

```bash
cd docker
docker compose down
docker compose up -d
```

Once this field is added, the Dify platform will allow the installation of all plugins that are not listed (and thus not verified) in the Dify Marketplace.

**Note**: For security reasons, always install plugins from unknown sources in a test or sandbox environment first. Confirm their safety before deploying to the production environment.
