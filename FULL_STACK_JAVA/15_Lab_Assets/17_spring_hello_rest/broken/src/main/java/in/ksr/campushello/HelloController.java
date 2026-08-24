package in.ksr.campushello;

import java.util.Map;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

// BROKEN: @Controller looks up a view name — JSON needs @RestController.
@Controller
public class HelloController {

    @GetMapping("/hello")
    public Map<String, String> hello() {
        return Map.of("message", "Hello, CampusCart");
    }

    @GetMapping("/health")
    public Map<String, String> health() {
        return Map.of("status", "UP", "app", "campus-hello-rest");
    }
}
