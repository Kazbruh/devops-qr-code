# Use the official Node.js 18 image with Alpine Linux as the base
FROM node:18-alpine AS base

# Set the working directory to /app
WORKDIR /app

# Copy the package files to the working directory
COPY package.json yarn.lock* package-lock.json* pnpm-lock.yaml* ./

# Install the dependencies
RUN \
    # If yarn.lock exists, install with yarn
    if [ -f yarn.lock ]; then yarn --frozen-lockfile; \
    # If package-lock.json exists, install with npm
    elif [ -f package-lock.json ]; then npm ci; \
    # If pnpm-lock.yaml exists, install with pnpm
    elif [ -f pnpm-lock.yaml ]; then corepack enable pnpm && pnpm i --frozen-lockfile; \
    # If no lockfile exists, exit with an error
    else echo "Lockfile not found." && exit 1; \
    fi

# Copy the source code to the working directory
COPY . .

# Build the application
RUN npm run build

# Expose the port 3000 for the server
EXPOSE 3000

# Set the default command to start the server
CMD [ "npm", "start" ]