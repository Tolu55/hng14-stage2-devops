# Stage 1: Builder
FROM node:18-slim AS BUILDER
WORKDIR /app
COPY package.json ./
RUN npm install --only=production

# Stage 2: Runtime
FROM node:18-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --gecos "" appuser
USER appuser

COPY --from=BUILDER --chown=appuser:appuser /app/node_modules ./node_modules
COPY --chown=appuser:appuser . .

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000 || exit 1

EXPOSE 3000
CMD ["node", "app.js"]
