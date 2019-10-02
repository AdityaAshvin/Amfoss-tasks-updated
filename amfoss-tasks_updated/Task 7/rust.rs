use regex::Regex;

fn main() 
{
let re : Regex = Regex::new( re r"^([a-zA-z0-9_\-\.]+)@([a-zA-z0-9_\-\.])\.([a-zA-Z]{2,5})$").unwrap();
if(re.is_match(text: "anyname@gmail.com")){}
println!("It is a valid email");
}
else{
	println(" Sorry! It is not a valid account ")
}
}
