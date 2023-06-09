/*
   Copyright 2018 Chaiyong Ragkhitwetsagul and Jens Krinke

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
 */

package crest.siamese.language;

import java.io.File;
import java.io.Reader;
import java.util.ArrayList;

public interface Tokenizer {
    public void configure(Normalizer normalizer);
    public ArrayList<String> tokenize(String s) throws Exception;
    public ArrayList<String> tokenize(Reader reader) throws Exception;
    public ArrayList<String> tokenizeLine(Reader reader) throws Exception;
    public ArrayList<String> tokenize(File f) throws Exception;
    public ArrayList<String> getTokensFromFile(String file) throws Exception;
    public ArrayList<String> getTokensFromString(String input) throws Exception;
}
