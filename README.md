# TowerOfBabelBot
Telegram bot for translation purposes 

## Environment variables:
- `TOKEN`: Bot API token from botfather;
- `LOGGING_LEVEL`: logging level (optional), default - `info`

## Deploy

### Create deployment package
- Clone this repository: `git clone https://github.com/Slamaio/TowerOfBabelBot.git`
- Run create-package bash script: `./create-package.sh`

### Create and configure API Gateway entrypoint
- Create and configure API Gateway entrypoint;
- Set webhook for your bot: follow the link through your browser or using curl – `https://api.telegram.org/bot{your_bot_api_token}/setWebhook?url={your_api_gateway_url}`
