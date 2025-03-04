#!/bin/bash

# Define project name
PROJECT_NAME=$1

# Create project directory structure
mkdir -p $PROJECT_NAME/src/main/java/com/example/servlets
mkdir -p $PROJECT_NAME/src/main/webapp/WEB-INF

# Create the web.xml file
cat > $PROJECT_NAME/src/main/webapp/WEB-INF/web.xml <<EOL
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://java.sun.com/xml/ns/javaee" version="3.0">
    <servlet>
        <servlet-name>HelloServlet</servlet-name>
        <servlet-class>com.example.servlets.HelloServlet</servlet-class>
    </servlet>
    <servlet>
        <servlet-name>GoodbyeServlet</servlet-name>
        <servlet-class>com.example.servlets.GoodbyeServlet</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>HelloServlet</servlet-name>
        <url-pattern>/hello</url-pattern>
    </servlet-mapping>
    <servlet-mapping>
        <servlet-name>GoodbyeServlet</servlet-name>
        <url-pattern>/goodbye</url-pattern>
    </servlet-mapping>
</web-app>
EOL

# Create HelloServlet.java
cat > $PROJECT_NAME/src/main/java/com/example/servlets/HelloServlet.java <<EOL
package com.example.servlets;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/hello")
public class HelloServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/plain");
        response.getWriter().println("Hello, World!");
    }
}
EOL

# Create GoodbyeServlet.java
cat > $PROJECT_NAME/src/main/java/com/example/servlets/GoodbyeServlet.java <<EOL
package com.example.servlets;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/goodbye")
public class GoodbyeServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/plain");
        response.getWriter().println("Goodbye, World!");
    }
}
EOL

# Print completion message
echo "Dummy Servlet project created in $PROJECT_NAME"
echo "Directory structure:"
tree $PROJECT_NAME

git -C $PROJECT_NAME add -A
git -C $PROJECT_NAME commit -m "init commit"