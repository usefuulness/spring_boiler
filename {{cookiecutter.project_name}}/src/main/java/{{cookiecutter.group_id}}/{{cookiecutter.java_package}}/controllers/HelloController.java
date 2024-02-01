package {{cookiecutter.group_id}}.{{cookiecutter.java_package}}.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HelloController {

    @GetMapping("/")
    public String hello(Model model) {
        model.addAttribute("contentTemplate", "hello");
        model.addAttribute("message", "Hello, World!");
        return "hello";
    }
}
