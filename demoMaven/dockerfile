# Start with a base image that has Java and Maven installed
FROM maven:3.6.3-openjdk-11-slim AS build

# Set working directory
WORKDIR /app

# Copy the source code into the container
COPY . .

# Build the application using Maven
RUN mvn clean install

# Start a new stage for the production image
FROM openjdk:11-jre-slim

# Set working directory
WORKDIR /app

# Copy the compiled application from the build stage
COPY --from=build /app/target/your-application.jar ./app.jar

# Expose the port your application runs on
EXPOSE 8080

# Command to run the application
CMD ["java", "-jar", "app.jar"]
