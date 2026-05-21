import java.util.*;

class SteramExample {
    public static void main(String[] args) {
        List<String> list = Arrays.asList("apple", "banana", "cherry", "date");

        // Using Stream to filter and print elements
        list.stream()
            .filter(s -> s.startsWith("b"))
            .forEach(System.out::println);
    }
}
public class second {
    public static void main(String[] args) {
       
    }
}


