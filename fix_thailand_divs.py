with open('thailand.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the extra </div>
# Look for:
#           </div>
#         </div>
#       </div>
#     </div>
#   </section>
#   <!-- FAQ Section -->
import re
content = re.sub(r'</div>\s*</div>\s*</div>\s*</section>\s*<!-- FAQ Section -->', '</div>\n    </div>\n  </section>\n\n  <!-- FAQ Section -->', content)

with open('thailand.html', 'w', encoding='utf-8') as f:
    f.write(content)
