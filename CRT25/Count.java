public class Count {
    public static String countandSay(int n) {
        if (n == 1) {
            return "1";
        }
        String s = countandSay(n - 1);
        StringBuilder sb = new StringBuilder();
        int i = 0;
        while (i < s.length()) {
            int count = 1;
            while (i + 1 < s.length() && s.charAt(i) == s.charAt(i + 1)) {
                count++;
                i++;
            }
            sb.append(count);
            sb.append(s.charAt(i));
            i++;
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        int n = 10;
        System.out.println(countandSay(n));
    }
}


