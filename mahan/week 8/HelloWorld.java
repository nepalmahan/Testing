// HelloWorldTest.java
import org.junit.Test;
import static org.junit.Assert.*;

public class HelloWorldTest {

    @Test
    public void testSayHello() {
        HelloWorld helloWorld = new HelloWorld();
        assertEquals("Hello, World!", helloWorld.sayHello());
    }
}
