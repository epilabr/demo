FROM openjdk:8
RUN mkdir /usr/src/demo
COPY /target/demo-0.0.1-SNAPSHOT.jar /usr/src/demo
WORKDIR /usr/src/demo
#RUN java -jar demo-0.0.1-SNAPSHOT.jar
CMD ["java", "-jar", "demo-0.0.1-SNAPSHOT.jar"]
