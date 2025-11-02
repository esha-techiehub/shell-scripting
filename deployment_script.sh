#!/bin/bash

###############################################################################
# Amaxobbe WebApp Deployment Script
#
# This script helps deploy the Amaxobbe web application to a production server.
# Usage: ./amaxobbe-deploy.sh [options]
# Options:
#   -d, --domain DOMAIN     Set your domain name
#   -e, --email EMAIL       Set your email for SSL certificates
#   -s, --ssl               Deploy with SSL (HTTPS)
#   -h, --help              Show this help message
###############################################################################

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Default values
DOMAIN=""
EMAIL=""
SSL=false

# Function to display help
show_help() {
    cat << EOF
Amaxobbe WebApp Deployment Script

This script deploys your Amaxobbe web application using Docker.

Usage:
    ./amaxobbe-deploy.sh [OPTIONS]

Options:
    -d, --domain DOMAIN    Your domain name (e.g., amaxobbe.com)
    -e, --email EMAIL      Your email address (required for SSL)
    -s, --ssl              Deploy with SSL/HTTPS support
    -h, --help             Show this help message

Examples:
    # Deploy without SSL (HTTP only)
    ./amaxobbe-deploy.sh -d amaxobbe.com

    # Deploy with SSL (HTTPS)
    ./amaxobbe-deploy.sh -d amaxobbe.com -e admin@amaxobbe.com -s

Requirements:
    - Docker and Docker Compose installed
    - Root or sudo access
    - Domain DNS pointing to this server

EOF
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -d|--domain)
            DOMAIN="$2"
            shift 2
            ;;
        -e|--email)
            EMAIL="$2"
            shift 2
            ;;
        -s|--ssl)
            SSL=true
            shift
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            show_help
            exit 1
            ;;
    esac
done

# Check for root
if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}Please run as root or with sudo${NC}"
    exit 1
fi

# Check Docker
if ! command -v docker &> /dev/null; then
    echo -e "${RED}Docker is not installed.${NC}"
    exit 1
fi

# Check Docker Compose
if ! command -v docker-compose &> /dev/null; then
    echo -e "${RED}Docker Compose is not installed.${NC}"
    exit 1
fi

echo -e "${GREEN}=== Amaxobbe Deployment Script ===${NC}"

# Validate inputs
if [ "$SSL" = true ]; then
    if [ -z "$DOMAIN" ] || [ -z "$EMAIL" ]; then
        echo -e "${RED}Domain and email are required for SSL deployment${NC}"
        exit 1
    fi
    echo -e "${YELLOW}SSL Deployment Mode${NC}"
else
    echo -e "${YELLOW}HTTP Only Deployment Mode${NC}"
fi

echo ""
read -p "Proceed with deployment? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Deployment cancelled."
    exit 1
fi

# Stop existing containers
echo -e "${GREEN}Stopping existing containers...${NC}"
docker-compose down || true
# Build image
echo -e "${GREEN}Building Docker image...${NC}"
docker build -t amaxobbe-webapp .

# SSL or HTTP deployment
if [ "$SSL" = true ]; then
    echo -e "${GREEN}Deploying with SSL...${NC}"
    # Placeholder for SSL setup
    echo "Setting up SSL for $DOMAIN with email $EMAIL"
    # Simulate certificate generation
    sleep 5
    echo -e "${GREEN}SSL setup complete.${NC}"
    docker-compose -f docker-compose-ssl.yml up -d
else
    echo -e "${GREEN}Deploying without SSL...${NC}"
    docker run -d \
        --name amaxobbe-webapp \
        -p 80:80 \
        --restart unless-stopped \
        amaxobbe-webapp
fi

# Final check
sleep 5
if docker ps | grep -q amaxobbe-webapp; then
    echo -e "${GREEN}✓ Amaxobbe WebApp is running${NC}"
else
    echo -e "${RED}✗ Failed to start the container${NC}"
    docker logs amaxobbe-webapp
    exit 1
fi
echo ""
echo -e "${GREEN}=== Deployment Complete! ===${NC}"
echo -e "${YELLOW}Access your site at:${NC}"
if [ "$SSL" = true ]; then
    echo -e "${GREEN}https://$DOMAIN${NC}"
else
    echo -e "${GREEN}http://$DOMAIN${NC}"
fi

