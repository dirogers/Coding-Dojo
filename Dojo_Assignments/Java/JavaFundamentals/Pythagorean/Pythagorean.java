import java.lang.Math;
public class Pythagorean {
    public double calculateHypotenuse(int legA, int legB) {
        // the hypotenuse is the side across from the right angle.
        double longLeg = Math.sqrt((legA*legA)+(legB*legB));
        // calculate the value of c given legA and legB
        return longLeg;
    }
}
