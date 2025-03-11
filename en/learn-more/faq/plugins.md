# Plugins

> The following issue and solution apply to version `1.0.0` **Community Edition**.

#### How to Handle Errors When Installing Plugins?

**Issue**: If you encounter the error message: `plugin verification has been enabled, and the plugin you want to install has a bad signature`, how to handle the issue?

**Solution**: Add the following line to the end of your `.env` configuration file: `FORCE_VERIFYING_SIGNATURE=false`

Once this field is added, the Dify platform will allow the installation of all plugins that are not listed (and thus not verified) in the Dify Marketplace.

**Note**: For security reasons, always install plugins from unknown sources in a test or sandbox environment first. Confirm their safety before deploying to the production environment.
