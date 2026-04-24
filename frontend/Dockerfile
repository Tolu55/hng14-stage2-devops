FROM node:18-slim as builder
WORKDIR /app
COPY package.json ./
RUN npm install --only=production

FROM node:18-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m appuser
USER appuser

COPY --from=builder --chown=appuser:appuser /app/node_modules ./node_modules
COPY --chown=appuser:appuser . .

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000 || exit 1

EXPOSE 3000
CMD ["node", "app.js"]
