# Parsing modes
There are two parsing modes available: <i>independent</i> and <i>composite</i>. You may find that one of the parsers is more or less convenient for your needs, but they are both capable of producing the same results.

## The Independent Parser
The name of the independent parser comes from the fact that you input the rhythm for each instrument in the drum set one at a time. This parsing mode is useful when you have a groove that is easier to think of one part at a time, or when different parts of the set need to use different subdivisions. When writing grooves with many parts, or some parts are sparsely used, you may find that the composite parser is more efficient as you will need to explicitly enter entire measures of rests when a part isn't used.

### Syntax
#### Rule and Token Definitions
<ul>
    <li><b>&lt;descriptor&gt;</b> - The shorthand descriptor of the instrument you are entering a rhythm for</li>
    <li><b>&lt;measure&gt;</b> - The rhythm string, where spaces (" ") are treated as rests, and letters (upper or lower case) are treated as audible notes. Letters and spaces are the only valid characters for this rule.</li>
    <li><b>:</b> - The separator character between the descriptor and rhythm</li>
    <li><b>|</b> - The measure delimiter character</li>
    <li><b>\n</b> - The newline character</li>
</ul>

#### Informal Grammar
COME BACK TO THIS
A groove is composed of one or more parts, separated by a newline character (\n), where a part follows the structure:
&lt;descriptor&gt;:(&lt;rhythm&gt;|)+\n;
Where (&lt;rhythm&gt;|)+ means that you must have one or more rhythm

#### EBNF
groove : ( descriptor ':' measure+ '\n' )+ ;
descriptor : 'h' | 'c' | 'C' | 'r' | 'R' | 's' | 'k' | '1' | '2' | '3' ;
measure : ( [a-zA-Z] | ' ' )+ '|' ;


## The Composite Parser
The name of the composite parser comes from the fact that you input the rhythm for each instrument in the drum set all at once, or in other words, your input string will be a composite of each part in the drum set. This parsing mode is faster when your groove uses many parts of the drum set, and when the parts in your groove tend to use the same subdivision. If there are parts of the drum set that your grooves uses very sparingly, you may find this mode more efficient, as you won't need to explicitly enter entire measures of rests when the part is not used.